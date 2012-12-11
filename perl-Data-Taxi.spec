%define upstream_name    Data-Taxi
%define upstream_version 0.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Taint-aware, XML-ish data serialization
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Debug::ShowStuff)
BuildArch:	noarch

%description
Taxi (*T*aint-*A*ware *X*ML-*I*sh) is a data serializer with several handy
features:

* Taint aware

  Taxi does not force you to trust the data you are serializing. None of
  the input data is executed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.960.0-2mdv2011.0
+ Revision: 656904
- rebuild for updated spec-helper

* Wed Nov 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.960.0-1mdv2011.0
+ Revision: 598320
+ rebuild (emptylog)

* Tue Jul 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.950.0-1mdv2011.0
+ Revision: 561167
- import perl-Data-Taxi


* Fri Oct 09 2009 cpan2dist 0.95-1mdv
- initial mdv release, generated with cpan2dist
