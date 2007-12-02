# Conditional build:
%bcond_with	bootstrap		# boostrap
#
%include	/usr/lib/rpm/macros.java
Summary:	DOM4J
Name:		dom4j
Version:	1.6.1
Release:	0.1
License:	BSD-style
Group:		Applications/Text
URL:		http://www.dom4j.org/
Source0:	http://dl.sourceforge.net/dom4j/%{name}-%{version}.tar.gz
# Source0-md5:	1e7ef6d20939315714de4a8502f27b2d
Source1:	%{name}-rundemo.sh
Patch0:		%{name}-build_xml.patch
%if %{with bootstrap}
BuildRequires:	jaxen-bootstrap >= 0:1.1-1
%else
#BuildRequires:	jaxen >= 0:1.1-2
%endif
BuildRequires:	ant >= 0:1.6
#BuildRequires:	bea-stax
#BuildRequires:	bea-stax-api
#BuildRequires:	isorelax
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	jtidy
BuildRequires:	junit
#BuildRequires:	junitperf
#BuildRequires:	msv-msv
#BuildRequires:	msv-xsdlib
#BuildRequires:	relaxngDatatype
BuildRequires:	rpmbuild(macros) >= 1.300
#BuildRequires:	ws-jaxme
BuildRequires:	xalan-j
BuildRequires:	xerces-j
BuildRequires:	xml-commons-apis
#BuildRequires:	xpp2
#BuildRequires:	xpp3
Requires:	isorelax
Requires:	msv-msv
Requires:	msv-xsdlib
Requires:	relaxngDatatype
Requires:	xerces-j2
Requires:	xpp2
Requires:	xpp3
%if %{with bootstrap}
Requires:	jaxen-bootstrap >= 0:1.1-1
%else
Requires:	jaxen >= 0:1.1-1
%endif
Requires:	bea-stax
Requires:	bea-stax-api
Requires:	ws-jaxme
Requires:	xalan-j2
Requires:	xml-commons-apis
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to
read, write, navigate, create and modify XML documents. dom4j
integrates with DOM and SAX and is seamlessly integrated with full
XPath support.

%package demo
Summary:	Samples for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description demo
Samples for %{name}.

%package manual
Summary:	Manual for %{name}
Group:		Documentation
Requires:	jpackage-utils

%description manual
Documentation for %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
# replace run.sh
cp %{SOURCE1} run.sh

%if "%{version}" == "1.6.1"
rm -f lib/endorsed/xml-apis-2.0.2.jar
#rm -f lib/test/jsr173_1.0_ri.jar
rm -f lib/test/junit-3.8.1.jar
#rm -f lib/test/junitperf-1.8.jar
#rm -f lib/tools/isorelax-20030108.jar
#rm -f lib/tools/jaxme-0.3.jar
#rm -f lib/tools/jaxme-js-0.3.jar
#rm -f lib/tools/jaxme-xs-0.3.jar
rm -f lib/tools/jtidy-4aug2000r7-dev.jar
rm -f lib/tools/xalan-2.5.1.jar
rm -f lib/tools/xercesImpl-2.6.2.jar
#rm -f lib/jaxen-1.1-beta-6.jar
#rm -f lib/jaxme-api-0.3.jar
#rm -f lib/jsr173_1.0_api.jar
#rm -f lib/msv-20030807.jar
#rm -f lib/pull-parser-2.1.10.jar
#rm -f lib/relaxngDatatype-20030807.jar
#rm -f lib/xpp3-1.1.3.3.jar
#rm -f lib/xsdlib-20030807.jar
rm -f dom4j-1.6.1.jar
%else
find -name '*.jar' | xargs rm -vf
%endif

# function matrix-concat not available
rm -f src/test/org/dom4j/xpath/MatrixConcatTest.java
# won't succeed in headless environment
rm src/test/org/dom4j/bean/BeansTest.java
# fix for deleted jars
sed -i -e '/unjar/d' -e 's|,cookbook/\*\*,|,|' build.xml
%patch0

%build
cd lib
#	ln -sf $(build-classpath xpp2)
#	ln -sf $(build-classpath relaxngDatatype)
	cd endorsed
		ln -sf $(build-classpath xml-commons-apis)
	cd ..
#	ln -sf $(build-classpath jaxme/jaxmeapi)
#	ln -sf $(build-classpath msv-xsdlib)
#	ln -sf $(build-classpath msv-msv)
#	ln -sf $(build-classpath jaxen)
#	ln -sf $(build-classpath bea-stax-api)
	cd test
#		ln -sf $(build-classpath bea-stax-ri)
#		ln -sf $(build-classpath junitperf)
		ln -sf $(build-classpath junit)
	cd ..
#	ln -sf $(build-classpath xpp3)
	cd tools
#		ln -sf $(build-classpath jaxme/jaxmexs)
		ln -sf $(build-classpath xalan)
#		ln -sf $(build-classpath jaxme/jaxmejs)
		ln -sf $(build-classpath jtidy)
#		ln -sf $(build-classpath isorelax)
#		ln -sf $(build-classpath jaxme/jaxme2)
		ln -sf $(build-classpath xercesImpl)
	cd ..
cd ..

%ant package samples test

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost

# manual
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf docs/apidocs
cp -a docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -a LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/classes/org/dom4j
cp -pr xml $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/src
cp -pr src/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/src
cp -pr build/classes/org/dom4j/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/classes/org/dom4j
cp -p run.sh $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}

%files demo
%defattr(644,root,root,755)
%{_datadir}/%{name}-%{version}
