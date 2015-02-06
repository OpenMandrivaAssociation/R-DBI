%global packname  DBI
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2.7
Release:          2
Summary:          R Database Interface
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/DBI_0.2-7.tar.gz
Requires:         R-methods 
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-methods 

%define debug_package %{nil}

%description
A database interface (DBI) definition for communication between R and
relational database management systems.  All classes in this package are
virtual and need to be extended by the various R/DBMS implementations.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2_5-1
+ Revision: 774952
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2_4-1
+ Revision: 774924
- Import R-DBI
- Import R-DBI


