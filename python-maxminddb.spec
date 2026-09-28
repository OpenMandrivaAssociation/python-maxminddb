Name:		python-maxminddb
Version:	3.2.0
Release:	1
Summary:	Reader for the MaxMind DB format
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/maxminddb/
Source0:	maxminddb-3.2.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	gcc
BuildRequires:	lib64python-devel
%description
Reader for the MaxMind DB format.

%files
%{python_sitearch}/*
