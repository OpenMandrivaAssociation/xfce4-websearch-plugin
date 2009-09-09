Summary:	A web search plugin for the Xfce panel
Name:		xfce4-websearch-plugin
Version:	0.1.1
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser) intltool
Obsoletes:	xfce-websearch-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
