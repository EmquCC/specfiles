Name: dbgate
Version: 5.2.1
Release: 1%{?dist}
Summary: Database management tool

Group: Applications/Databases
License: MIT
URL: https://github.com/dbgate/dbgate

Source0: https://github.com/dbgate/dbgate/archive/v%{version}.tar.gz

BuildRequires: binutils, git, python2, gcc, gcc-c++, yarnpkg, bsdtar, jq, zlib, xz
BuildRequires: nodejs12, ca-certificates, xz, git-lfs

%description
dbgate is a database management tool that allows you to connect to multiple databases, run queries, and manage your data.

%prep
%setup -q

%build
yarn
yarn build:app:local

%install
install -d %{buildroot}%{_bindir}
cp -r app/dist/* %{buildroot}%{_bindir}

%files
%{_bindir}/*

%changelog
* Fri Jan 06 2023 Jan Prochazka <dunno@dunno.lol> 5.2.1-1
- FIXED: client_id param in OAuth
- ADDED: OAuth scope parameter
- FIXED: login page - password was not sent, when submitting by pressing ENTER
- FIXED: Used permissions fix
- FIXED: Export modal - fixed crash when selecting different database
