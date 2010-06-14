# TODO:
# - build from source. See SOURCE branch for unfinished work.
%define		srcname	dom4j
%include	/usr/lib/rpm/macros.java
Summary:	DOM4J - Open Source XML framework for Java
Summary(pl.UTF-8):	Szkielet XML z otwartymi źródłami dla Javy
Name:		java-%{srcname}
Version:	1.6.1
Release:	0.1
License:	BSD-style
Group:		Applications/Text
Source0:	http://sourceforge.net/projects/dom4j/files/dom4j/1.6.1/dom4j-1.6.1.jar
# Source0-md5:	1e7ef6d20939315714de4a8502f27b2d
Source1:	%{srcname}-rundemo.sh
URL:		http://www.dom4j.org/
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

%prep
%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{SOURCE0}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
