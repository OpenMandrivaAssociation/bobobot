%define	name	bobobot
%define	version	0
%define preview preview3
%define rel %mkrel 4
%define release	16.%{preview}.%rel
%define	Summary	Mario-like game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/bobobot/bobobot-preview3.tar.bz2
Url:		http://newbreedsoftware.com/bobobot/
License:	GPLv2+
Group:		Games/Arcade
BuildRequires:	SDL_mixer-devel X11-devel alsa-lib-devel esound-devel ImageMagick
Patch0:		%{name}-preview3-fix-makefile.patch.bz2
Patch2:		%{name}-preview3-fix-nosound.patch.bz2

%description
BoboBot is a multi-level one-player action game starring "BoboBot," the
robo-monkey. It's played with the keyboard, or optionally with a joystick

%prep
%setup -q -n %{name}-preview3
%patch0 -p1
%patch2 -p1 -z .pix

# beurk
chmod +x mods/unused
chmod -R a+r *

%build
%make SOUND=YES MUSIC=YES INSTALLROOT=%{_gamesdatadir}/%{name} OPTIMIZE="%{optflags}" X11_LIB="-L/usr/X11R6/%_lib -lX11" bobobot

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}
convert %{name}-icon.xpm -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert %{name}-icon.xpm -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert %{name}-icon.xpm -size 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=BoboBot
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -d $RPM_BUILD_ROOT{%{_gamesbindir},%{_gamesdatadir}/%{name}}
make INSTALLROOT=$RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
mv $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_gamesbindir}

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}

