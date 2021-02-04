Name:           disorderfs
Version:        0.5.10
Release:        2%{?dist}
Summary:        FUSE filesystem that introduces non-determinism

License:        GPLv3+
Source0:        https://salsa.debian.org/reproducible-builds/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  pkg-config
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  fuse
BuildRequires:  bc

Requires:       fuse

%description
disorderfs is an overlay FUSE filesystem that introduces non-determinism
into filesystem metadata.  For example, it can randomize the order
in which directory entries are read.  This is useful for detecting
non-determinism in the build process.

%prep
%autosetup -n %{name}-%{version}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=/usr

%check
make -C tests test || true

%files
%doc README
%license COPYING
%{_bindir}/disorderfs
%{_datadir}/man/man1/disorderfs.1.gz

%changelog
* Thu Feb 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-2
- Update spec and add tests.

* Mon Jan 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 0.5.10-1
- Initial RPM packaging.
