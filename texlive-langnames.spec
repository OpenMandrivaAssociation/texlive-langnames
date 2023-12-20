Name:		texlive-langnames
Version:	69101
Release:	1
Summary:	Name languages and their genetic affiliations consistently
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/langnames
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package attempts to make the typing of language names,
codes, and families slightly easier by providing macros to
access pre-defined language--code--family combinations from two
important databases, as well as the possibility to create new
combinations. It may be particularly useful for large,
collaborative projects as well as typologically minded ones
with a variety of language examples.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/langnames
%{_texmfdistdir}/tex/latex/langnames
%doc %{_texmfdistdir}/doc/latex/langnames

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
