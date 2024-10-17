%define preview preview3

Summary:	Mario-like game
Name:		bobobot
Version:	0
Release:	16.%{preview}.9
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/bobobot/bobobot-preview3.tar.bz2
Url:		https://newbreedsoftware.com/bobobot/
License:	GPLv2+
Group:		Games/Arcade
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(x11)
BuildRequires:	imagemagick
Patch0:		%{name}-preview3-fix-makefile.patch
Patch2:		%{name}-preview3-fix-nosound.patch

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
%make SOUND=YES MUSIC=YES INSTALLROOT=%{_gamesdatadir}/%{name} OPTIMIZE="%{optflags}" X11_LIB="-L%_libdir -lX11" bobobot CC="gcc %ldflags"

%install
%{__install} -d %{buildroot}{%{_liconsdir},%{_miconsdir}}
convert %{name}-icon.xpm -size 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert %{name}-icon.xpm -size 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert %{name}-icon.xpm -size 48x48 %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=BoboBot
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -d %{buildroot}{%{_gamesbindir},%{_gamesdatadir}/%{name}}
make INSTALLROOT=%{buildroot}%{_gamesdatadir}/%{name}
mv %{buildroot}%{_gamesdatadir}/%{name}/%{name} %{buildroot}%{_gamesbindir}

%files
%doc docs/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
