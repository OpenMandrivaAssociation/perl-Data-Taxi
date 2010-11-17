%define upstream_name    Data-Taxi
%define upstream_version 0.96

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Taint-aware, XML-ish data serialization
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Debug::ShowStuff)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Taxi (*T*aint-*A*ware *X*ML-*I*sh) is a data serializer with several handy
features:

* Taint aware

  Taxi does not force you to trust the data you are serializing. None of
  the input data is executed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


