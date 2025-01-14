Name:		texlive-biber
Version:	70724
Release:	1
Summary:	A BibTeX replacement for users of biblatex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/biber
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Biber is a BibTeX replacement for users of biblatex. Biber
supports full UTF-8, can (re)-encode input and output, supports
highly configurable sorting, dynamic bibliography sets and many
other features. The CTAN distribution offers a compressed tar
archive of the sources, etc., together with "binary"
distributions for a variety of platforms. Note: on SourceForge
biber is formally named "biblatex-biber", to distinguish it
from an earlier (now apparently moribund) project called
"biber".

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/bibtex/biber
#- source
%doc %{_texmfdistdir}/source/bibtex/biber

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
