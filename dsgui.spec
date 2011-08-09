Summary:	dsgui is a free graphical interface for 'Datove schranky'
Name:		dsgui
Version:	1.6.2
Release:	%mkrel 1
Source0:	%{name}-%{version}.tar.gz
License:	LGPL
Group:		Office
BuildArch:	noarch
Requires:	dslib >= 1.6
BuildRequires:	python
BuildRequires:	python-setuptools
Requires:	pygtk2
Requires:	python-reportlab
Requires:	python-sqlalchemy
URL:		http://labs.nic.cz/datove-schranky/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
dsgui is a GUI application allowing access to a 'Databox' - an 
electronic communication interface endorsed by the Czech government.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version} -q
sed -i 's/Office/Office;/g' dsgui.desktop

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
