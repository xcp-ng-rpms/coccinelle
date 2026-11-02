Name:           coccinelle
Version:        1.2
Release:        3%{?dist}
Summary:        Semantic patching for Linux (spatch)
License:        GPL-2.0-only
URL:            https://github.com/coccinelle/coccinelle
Source0:        https://github.com/coccinelle/coccinelle/archive/refs/tags/coccinelle-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml >= 3.12.0

# We need to mark some modules in coccinelle sources. Otherwise the automatic 
# OCaml dependency generator will generate a wrong graph, and prevent the 
# installation of the generated RPM by claiming that "Requires" are missing.
%global __ocaml_requires_opts \
-i Control_flow_c \
-i Cpp_token_c \
-i Lexer_parser \
-i Ograph_extended \
-i Parsing_stat \
-i Token_annot \
-i Token_views_c \
%{nil}

%description
Coccinelle is a program matching and transformation engine which
provides the language SmPL (Semantic Patch Language) for specifying 
desired matches and transformations in C code.

%prep
%autosetup -p1

%build
./autogen
%configure
make

%install
%make_install

%files
%doc %{_mandir}/man1/pycocci.1.gz
%doc %{_mandir}/man1/spatch.1.gz
%doc %{_mandir}/man1/spgen.1.gz
%doc %{_mandir}/man3/Coccilib.3cocci.gz
%{_bindir}/spatch
%{_bindir}/spgen
%{_libdir}/%{name}/dllpyml_stubs.so
%{_libdir}/%{name}/ocaml/*.cmi
%{_libdir}/%{name}/ocaml/*.cmx
%{_libdir}/%{name}/python/coccilib/*.py
%{_libdir}/%{name}/python/coccilib/*.pyc
%{_libdir}/%{name}/python/coccilib/*.pyo
%{_libdir}/%{name}/standard.h
%{_libdir}/%{name}/standard.iso
%{_datadir}/bash-completion/completions/spatch

%changelog
* Mon Nov 02 2026 Alexandre Sollier <alexandre.sollier@vates.tech> - 1.2-3
- Rebuild to sync with ocaml-4.14.4
- Use macros to invoke `configure` and list `/usr/lib` files

* Mon Oct 28 2024 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.2-2
- Rebuild to sync with ocaml-4.14.2

* Mon Jul 15 2024 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.2-1
- Initial package
