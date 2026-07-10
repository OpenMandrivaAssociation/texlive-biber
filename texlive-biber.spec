%global tl_name biber
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.21
Release:	%{tl_revision}.1
Summary:	A BibTeX replacement for users of BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/biber/base
License:	artistic2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(biber.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Biber is a BibTeX replacement for users of BibLaTeX. Biber supports full
UTF-8, can (re)-encode input and output, supports highly configurable
sorting, dynamic bibliography sets and many other features. The CTAN
distribution offers a compressed tar archive of the sources, etc.,
together with "binary" distributions for a variety of platforms. Note:
on SourceForge biber is formally named "biblatex-biber", to distinguish
it from an earlier (now apparently moribund) project called "biber".

