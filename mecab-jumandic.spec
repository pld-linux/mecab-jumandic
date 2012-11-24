Summary:	Juman dictionary for Mecab
Summary(pl.UTF-8):	Słownik Juman dla biblioteki Mecab
Name:		mecab-jumandic
Version:	5.1
%define	subver	20070304
# base 1 as it's post-release, not pre-release
Release:	1.%{subver}.1
License:	BSD
Group:		Libraries
#Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	803da9a299712ef68316911a9c7d865e
URL:		http://code.google.com/p/mecab/
BuildRequires:	mecab-devel >= 0.994
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Juman dictionary for Mecab.

%description -l pl.UTF-8
Słownik Juman dla biblioteki Mecab.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%{_libdir}/mecab/dic/jumandic
