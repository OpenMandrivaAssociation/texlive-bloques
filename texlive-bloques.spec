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
Requires(post):	texlive-tlpkg
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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bloques/bloques.sty
%doc %{_texmfdistdir}/doc/latex/bloques/README
%doc %{_texmfdistdir}/doc/latex/bloques/example.pdf
%doc %{_texmfdistdir}/doc/latex/bloques/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
