# TODO:
# - build from source. See SOURCE branch for unfinished work.
 
%include	/usr/lib/rpm/macros.java
%define		srcname	dom4j
 
Summary:	DOM4J - Open Source XML framework for Java
Summary(pl.UTF-8):	Szkielet XML z otwartymi źródłami dla Javy
Name:		java-dom4j
Version:	1.6.1
Release:	0.1
License:	BSD-style
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/project/dom4j/dom4j/1.6.1/dom4j-%{version}.jar
# Source0-md5:	4d8f51d3fe3900efc6e395be48030d6d
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
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
