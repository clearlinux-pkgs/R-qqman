#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-qqman
Version  : 0.1.4
Release  : 11
URL      : https://cran.r-project.org/src/contrib/qqman_0.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/qqman_0.1.4.tar.gz
Summary  : Q-Q and Manhattan Plots for GWAS Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-calibrate
BuildRequires : R-calibrate
BuildRequires : buildreq-R

%description
# qqman: An R package for creating Q-Q and manhattan plots from GWAS results.
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/qqman)](http://cran.r-project.org/package=qqman)

%prep
%setup -q -c -n qqman

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552811042

%install
export SOURCE_DATE_EPOCH=1552811042
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qqman
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qqman
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qqman
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  qqman || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/qqman/DESCRIPTION
/usr/lib64/R/library/qqman/INDEX
/usr/lib64/R/library/qqman/Meta/Rd.rds
/usr/lib64/R/library/qqman/Meta/data.rds
/usr/lib64/R/library/qqman/Meta/features.rds
/usr/lib64/R/library/qqman/Meta/hsearch.rds
/usr/lib64/R/library/qqman/Meta/links.rds
/usr/lib64/R/library/qqman/Meta/nsInfo.rds
/usr/lib64/R/library/qqman/Meta/package.rds
/usr/lib64/R/library/qqman/Meta/vignette.rds
/usr/lib64/R/library/qqman/NAMESPACE
/usr/lib64/R/library/qqman/NEWS.md
/usr/lib64/R/library/qqman/R/qqman
/usr/lib64/R/library/qqman/R/qqman.rdb
/usr/lib64/R/library/qqman/R/qqman.rdx
/usr/lib64/R/library/qqman/data/Rdata.rdb
/usr/lib64/R/library/qqman/data/Rdata.rds
/usr/lib64/R/library/qqman/data/Rdata.rdx
/usr/lib64/R/library/qqman/doc/index.html
/usr/lib64/R/library/qqman/doc/qqman.R
/usr/lib64/R/library/qqman/doc/qqman.Rmd
/usr/lib64/R/library/qqman/doc/qqman.html
/usr/lib64/R/library/qqman/help/AnIndex
/usr/lib64/R/library/qqman/help/aliases.rds
/usr/lib64/R/library/qqman/help/paths.rds
/usr/lib64/R/library/qqman/help/qqman.rdb
/usr/lib64/R/library/qqman/help/qqman.rdx
/usr/lib64/R/library/qqman/html/00Index.html
/usr/lib64/R/library/qqman/html/R.css
