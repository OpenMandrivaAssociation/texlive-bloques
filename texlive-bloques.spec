%global tl_name bloques
%global tl_revision 22490

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Generate control diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/bloques
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bloques.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bloques.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses TikZ to provide commands for generating control
diagrams (specially in power electronics).

