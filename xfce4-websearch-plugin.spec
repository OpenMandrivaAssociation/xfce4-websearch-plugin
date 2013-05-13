Summary:	A web search plugin for the Xfce panel
Name:		xfce4-websearch-plugin
Version:	0.1.1
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	pkgconfig(libxfcegui4-1.0) >= 4.4.2
BuildRequires:	perl(XML::Parser) intltool
Obsoletes:	xfce-websearch-plugin

%description
A web search plugin for the Xfce panel.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS COPYING AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/websearch.desktop


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-5mdv2010.0
+ Revision: 435107
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-4mdv2009.0
+ Revision: 262415
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-3mdv2009.0
+ Revision: 257015
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 119329
- Fix tarball
- New release 0.1.1

* Thu Dec 06 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.0-1mdv2008.1
+ Revision: 115812
- Add BuildRequires
- import xfce4-websearch-plugin


