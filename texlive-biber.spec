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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/biber
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/biber/biber.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/Changes
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-cygwin
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-freebsd
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-linux
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-linux-aarch64
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-linux-musl
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-macos
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.biber-windows
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/biblatex-biber.tar.gz
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/biber/utf8-macro-map.html
