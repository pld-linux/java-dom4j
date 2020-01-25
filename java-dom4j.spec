# TODO
# - tests: org.dom4j.io.StaxTest failed
#
# Conditional build:
%bcond_with		bootstrap	# boostrap
%bcond_without	javadoc		# don't build javadoc
%bcond_with		tests		# don't build and run tests

%define		srcname	dom4j
Summary:	DOM4J - Open Source XML framework for Java
Summary(pl.UTF-8):	Szkielet XML z otwartymi źródłami dla Javy
Name:		java-dom4j
Version:	1.6.1
Release:	2
License:	BSD-style
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/dom4j/%{srcname}-%{version}.tar.gz
# Source0-md5:	1e7ef6d20939315714de4a8502f27b2d
Source1:	%{srcname}-rundemo.sh
Patch0:		%{srcname}-build_xml.patch
Patch1:		dom4j-java5.patch
URL:		http://www.dom4j.org/
%if %{with bootstrap}
BuildRequires:	jaxen-bootstrap >= 1.1-1
%else
#BuildRequires:	jaxen >= 1.1-2
%endif
BuildRequires:	ant >= 1.6
#BuildRequires:	bea-stax
#BuildRequires:	bea-stax-api
#BuildRequires:	isorelax
BuildRequires:	java(jaxp_parser_impl)
BuildRequires:	java-jaxme
BuildRequires:	java-junit
BuildRequires:	java-xalan
BuildRequires:	java-xml-commons
BuildRequires:	jpackage-utils >= 1.6
BuildRequires:	jtidy
#BuildRequires:	junitperf
#BuildRequires:	msv-msv
#BuildRequires:	msv-xsdlib
#BuildRequires:	relaxngDatatype
BuildRequires:	rpmbuild(macros) >= 1.300
#BuildRequires:	xpp2
#BuildRequires:	xpp3
#Requires:	bea-stax
#Requires:	bea-stax-api
#Requires:	isorelax
Requires:	java(jaxp_parser_impl)
Requires:	java-jaxme
Requires:	java-xalan
Requires:	java-xml-commons
#Requires:	msv-msv
#Requires:	msv-xsdlib
#Requires:	relaxngDatatype
#Requires:	xpp2
#Requires:	xpp3
%if %{with bootstrap}
Requires:	jaxen-bootstrap >= 0:1.1-1
%else
#Requires:	jaxen >= 0:1.1-1
%endif
Obsoletes:	dom4j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to
read, write, navigate, create and modify XML documents. dom4j
integrates with DOM and SAX and is seamlessly integrated with full
XPath support.

%description -l pl.UTF-8
dom4j to szkielet XML z otwartymi źródłami dla Javy. Pozwala na
odczyt, zapis, nawigację i modyfikowanie dokumentów XML. Integruje się
z DOM i SAX, jest w sposób przezroczysty zintegrowany z pełną obsługą
XPath.

%package demo
Summary:	Samples for %{srcname}
Summary(pl.UTF-8):	Przykłady do pakietu %{srcname}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:	dom4j-demo

%description demo
Samples for %{srcname}.

%description demo -l pl.UTF-8
Przykłady do pakietu %{srcname}.

%package manual
Summary:	Manual for %{srcname}
Summary(pl.UTF-8):	Podręcznik do pakietu %{srcname}
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	dom4j-manual

%description manual
Documentation for %{srcname}.

%description manual -l pl.UTF-8
Podręcznik do pakietu %{srcname}.

%package javadoc
Summary:	Javadoc for %{srcname}
Summary(pl.UTF-8):	Dokumentacja Javadoc do pakietu %{srcname}
Group:		Documentation
Obsoletes:	dom4j-javadoc

%description javadoc
Javadoc for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}
# replace run.sh
install -p %{SOURCE1} run.sh

%if "%{version}" == "1.6.1"
rm -f lib/endorsed/xml-apis-2.0.2.jar
#rm -f lib/test/jsr173_1.0_ri.jar
rm -f lib/test/junit-3.8.1.jar
#rm -f lib/test/junitperf-1.8.jar
#rm -f lib/tools/isorelax-20030108.jar
rm -f lib/tools/jaxme-0.3.jar
rm -f lib/tools/jaxme-js-0.3.jar
rm -f lib/tools/jaxme-xs-0.3.jar
rm -f lib/tools/jtidy-4aug2000r7-dev.jar
rm -f lib/tools/xalan-2.5.1.jar
rm -f lib/tools/xercesImpl-2.6.2.jar
#rm -f lib/jaxen-1.1-beta-6.jar
rm -f lib/jaxme-api-0.3.jar
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
%undos build.xml
%patch0 -p0
%undos -f java
%patch1 -p1

rm -rf docs/apidocs

%build
cd lib
#	ln -sf $(find-jar xpp2)
#	ln -sf $(find-jar relaxngDatatype)
	cd endorsed
		ln -sf $(find-jar xml-commons-apis)
	cd ..
	ln -sf $(find-jar jaxme/jaxmeapi)
#	ln -sf $(find-jar msv-xsdlib)
#	ln -sf $(find-jar msv-msv)
#	ln -sf $(find-jar jaxen)
#	ln -sf $(find-jar bea-stax-api)
	cd test
#		ln -sf $(find-jar bea-stax-ri)
#		ln -sf $(find-jar junitperf)
		ln -sf $(find-jar junit)
	cd ..
#	ln -sf $(find-jar xpp3)
	cd tools
		ln -sf $(find-jar jaxme/jaxmexs)
		ln -sf $(find-jar xalan)
		ln -sf $(find-jar jaxme/jaxmejs)
		ln -sf $(find-jar jtidy)
#		ln -sf $(find-jar isorelax)
		ln -sf $(find-jar jaxme/jaxme2)
		ln -sf $(find-jar xercesImpl)
	cd ..
cd ..

%ant package samples %{?with_javadoc:javadoc} %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost
%endif

# manual
install -d $RPM_BUILD_ROOT%{_docdir}/%{srcname}-manual-%{version}
cp -a docs/* $RPM_BUILD_ROOT%{_docdir}/%{srcname}-manual-%{version}

# demo
install -d $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}/classes/org/dom4j
cp -a xml $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}
install -d $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}/src
cp -a src/samples $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}/src
cp -a build/classes/org/dom4j/samples $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}/classes/org/dom4j
install -p run.sh $RPM_BUILD_ROOT%{_datadir}/%{srcname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar

%files demo
%defattr(644,root,root,755)
%{_datadir}/%{srcname}-%{version}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}

%files manual
%defattr(644,root,root,755)
%{_docdir}/%{srcname}-manual-%{version}
