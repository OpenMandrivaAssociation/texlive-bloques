# revision 22490
# category Package
# catalog-ctan /graphics/pgf/contrib/bloques
# catalog-date 2011-05-15 09:47:34 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bloques
Version:	1.0
Release:	1
Summary:	Generate control diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/bloques
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bloques.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bloques.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package uses TikZ to provide commands for generating
control diagrams (specially in power electronics).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bloques/bloques.sty
%doc %{_texmfdistdir}/doc/latex/bloques/README
%doc %{_texmfdistdir}/doc/latex/bloques/example.pdf
%doc %{_texmfdistdir}/doc/latex/bloques/example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
