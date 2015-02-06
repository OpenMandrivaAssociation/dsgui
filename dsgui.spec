Summary:	Free graphical interface for 'Datove schranky'
Name:		dsgui
Version:	1.6.3
%define subrel	1
Release:	2
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

%description
dsgui is a GUI application allowing access to a 'Databox' - an 
electronic communication interface endorsed by the Czech government.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version} -q
sed -i 's/Office/Office;/g' dsgui.desktop

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed \
	--root=%{buildroot} 

%find_lang %{name}

%clean

%files -f %{name}.lang
%defattr(-,root,root,-)
%dir %{py_puresitedir}/%{name}*
%{py_puresitedir}/%{name}*/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}*
%{_datadir}/icons/hicolor/*/apps/%{name}*


%changelog
* Sat Oct 15 2011 Tomas Kindl <supp@mandriva.org> 1.6.3-0.1mdv2011.0
+ Revision: 704784
- update to 1.6.3

* Sun May 29 2011 Tomas Kindl <supp@mandriva.org> 1.5.1-1
+ Revision: 681703
-update to 1.5.1

* Thu May 05 2011 Tomas Kindl <supp@mandriva.org> 1.5-1
+ Revision: 669309
- update to 1.5

* Tue Apr 26 2011 Tomas Kindl <supp@mandriva.org> 1.4.1-2
+ Revision: 659490
- force rebuild

* Thu Apr 21 2011 Tomas Kindl <supp@mandriva.org> 1.4.1-1
+ Revision: 656559
- add missing python require
- fix license, group, python macros...
- import dsgui


