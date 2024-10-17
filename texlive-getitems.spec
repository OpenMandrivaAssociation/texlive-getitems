Name:		texlive-getitems
Version:	39365
Release:	2
Summary:	Gathering items from a list-like environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/getitems
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getitems.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getitems.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getitems.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a \gatheritems command to parse a list of
data separated by \item tokens. This makes it easier to define
custom environments which structure their data in the same way
that itemize or enumerate do.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/getitems
%{_texmfdistdir}/tex/latex/getitems
%doc %{_texmfdistdir}/doc/latex/getitems

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
