%global tl_name langnames
%global tl_revision 69101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	Name languages and their genetic affiliations consistently
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/langnames
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langnames.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package attempts to make the typing of language names, codes, and
families slightly easier by providing macros to access pre-defined
language--code--family combinations from two important databases, as
well as the possibility to create new combinations. It may be
particularly useful for large, collaborative projects as well as
typologically minded ones with a variety of language examples.

