#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-plugin-registry
Version  : 2.0.6
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.jar
Source9  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.jar
Source11  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.jar
Source13  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.jar
Source14  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.jar
Source17  : https://repo1.maven.org/maven2/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-plugin-registry-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-plugin-registry package.
Group: Data

%description data
data components for the mvn-maven-plugin-registry package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.10/maven-plugin-registry-2.0.10.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.11/maven-plugin-registry-2.0.11.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.6/maven-plugin-registry-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.7/maven-plugin-registry-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.8/maven-plugin-registry-2.0.8.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.0.9/maven-plugin-registry-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.0/maven-plugin-registry-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-plugin-registry/2.2.1/maven-plugin-registry-2.2.1.pom
