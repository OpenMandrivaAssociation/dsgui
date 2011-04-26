%define unmangled_version	1.4.1

Summary:	dsgui is a free graphical interface for 'Datove schranky'
Name:		dsgui
Version:	1.4.1
Release:	%mkrel 2
Source0:	%{name}-%{unmangled_version}.tar.gz
License:	LGPL
Group:		Office
BuildArch:	noarch
Requires:	dslib >= 1.4.1 
BuildRequires:	python
BuildRequires:  python-setuptools
Requires:	pygtk2
Requires:	python-reportlab
Requires:	python-sqlalchemy
URL:		http://labs.nic.cz/datove-schranky/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
dsgui is a GUI application allowing access to a 'Databox' - an 
electronic communication interface endorsed by the Czech government.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version} -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed \
	--root=%{buildroot} 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%dir %{py_puresitedir}/%{name}*
%{py_puresitedir}/%{name}*/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}*
%{_datadir}/icons/hicolor/*/apps/%{name}*


