# revision 23715
# category Package
# catalog-ctan /biblio/biber
# catalog-date 2011-08-24 12:15:15 +0200
# catalog-license artistic
# catalog-version 0.9.5
Name:		texlive-biber
Version:	0.9.5
Release:	1
Summary:	A BibTeX replacement for users of biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/biber
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biber.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-biber.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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
%doc %{_texmfdistdir}/doc/bibtex/biber/biber.pdf
#- source
%doc %{_texmfdistdir}/source/bibtex/biber/README
%doc %{_texmfdistdir}/source/bibtex/biber/biblatex-biber.tar.gz
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
