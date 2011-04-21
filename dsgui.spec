%define name	dsgui
%define version	1.4.1
%define unmangled_version	1.4.1
%define release	1
%include %{_rpmconfigdir}/macros.python

Summary:	dsgui is a free graphical interface for 'Datove schranky'
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{unmangled_version}.tar.gz
License:	GNU LGPL
Group:		Development/Libraries
BuildArch:	noarch
Requires:	dslib >= 1.4.1 
Requires:	pygtk2
Requires:	python-reportlab
Requires:	python-sqlalchemy
URL:		http://labs.nic.cz/datove-schranky/

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
%dir %{py_sitedir}/%{name}*
%{py_sitedir}/%{name}*/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}*
%{_datadir}/icons/hicolor/*/apps/%{name}*


