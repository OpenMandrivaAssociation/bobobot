%define preview preview3

Summary:	Mario-like game
Name:		bobobot
Version:	0
Release:	16.%{preview}.9
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/bobobot/bobobot-preview3.tar.bz2
Url:		http://newbreedsoftware.com/bobobot/
License:	GPLv2+
Group:		Games/Arcade
Buildrequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
Buildrequires:	pkgconfig(x11)
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

%clean

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



%changelog
* Wed Jan 05 2011 Funda Wang <fwang@mandriva.org> 0-16.preview3.8mdv2011.0
+ Revision: 628658
- tighten BR

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0-16.preview3.7mdv2011.0
+ Revision: 571832
- bunzip2 the patches

* Tue Jun 16 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 0-16.preview3.7mdv2010.0
+ Revision: 386379
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0-16.preview3.6mdv2009.0
+ Revision: 243357
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Funda Wang <fwang@mandriva.org> 0-16.preview3.4mdv2008.1
+ Revision: 116845
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel
    - import bobobot


* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0-16.preview3.3mdv2007.0
- switch to XDG menu

* Thu May  5 2005 Pixel <pixel@mandriva.com> 0-16.preview3.2mdk
- fix build on lib64 (hopefully)

* Thu Mar 24 2005 Olivier Thauvin <nanardon@mandrake.org> 0-16.preview3.1mdk
- who is the stupid guy who didn't put mdk at the end of release tag ?

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 0-15mdk.preview3
- rebuild

* Wed Aug 06 2003 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0-14mdk.preview3
- include more meaningful documentation

* Mon Aug 04 2003 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0-13mdk.preview3
- rebuild
- move stuff to %%{_gamesbindir} & %%{_gamesdatadir}
- quiet setup
- drop Prefix tag
- cosmetics
- added menu item
- added icons

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0-12mdk.preview3
- rebuild

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 0-11mdk.preview3
- recompile against new vorbis stuff

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 0-10mdk.preview3
- rebuild for new libasound (alsa)

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 0-9mdk.preview3
- BuildRequires

* Tue Sep 11 2001 Stefan van der Eijk <stefan@eijk.nu> 0-8mdk.preview3
- BuildRequires: libSDL1.2-devel XFree86-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0-7mdk.preview3
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0-6mdk.preview3
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0-5mdk.preview3
- rebuild for new lib mixer

* Mon Dec  4 2000 Pixel <pixel@mandrakesoft.com> 0-4mdk.preview3
- new version

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0-3mdk.preview2
- rebuild

* Mon Nov 27 2000 Pixel <pixel@mandrakesoft.com> 0-2mdk.preview2
- add BuildRequires

* Wed Nov  1 2000 Pixel <pixel@mandrakesoft.com> 0-1mdk.preview2
- initial spec


# end of file
