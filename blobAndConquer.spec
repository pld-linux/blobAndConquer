Summary:	3D action game
Summary(pl.UTF-8):	Trójwymiarowa gra akcji
Name:		blobAndConquer
Version:	1.07
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
# download it from http://www.parallelrealities.co.uk/projects/blobAndConquer.php
# and put it into the blobAndConquer dir
Source0:	%{name}-%{version}-1.tar.gz
# Source0-md5:	b51cee505c1aacb21c7bb2ff57531aeb
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.parallelrealities.co.uk/projects/blobAndConquer.php
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mission and Objective based 3D Action game. This is episode 2 of the
Blob Wars saga.

%description -l pl.UTF-8
Trójwymiarowa gra akcji oparta na wykonywaniu misji i zadań. Jest to
drugi epizod sagi Blob Wars.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/blobAndConquer.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/blobAndConquer.pak
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/32x32/apps/blobAndConquer.png
%{_pixmapsdir}/%{name}.png
