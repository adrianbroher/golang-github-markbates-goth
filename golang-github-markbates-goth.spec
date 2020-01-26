# Generated by go2rpm 1
%bcond_without check

# https://github.com/markbates/goth
%global goipath         github.com/markbates/goth
Version:                1.61.0

%gometa

%global common_description %{expand:
Package goth provides a simple, clean, and idiomatic way to write
authentication packages for Go web applications.}

%global golicenses      LICENSE.txt
%global godocs          examples README.md providers/faux/README.md\\\
                        providers/nextcloud/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package goth provides a simple, clean, and idiomatic way to write authentication packages for Go web applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Replace the github.com/gorilla/pat dependency with github.com/gorilla/mux
# gorilla/pat seems to be unmaintained.  It is also only a convenience wrapper
# around gorilla/mux, which is also already packaged for Fedora
Patch0:         replace-pat-with-mux.patch

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/gorilla/sessions)
BuildRequires:  golang(github.com/lestrrat-go/jwx/jwk)
BuildRequires:  golang(github.com/markbates/going/defaults)
BuildRequires:  golang(github.com/mrjones/oauth)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Jan 25 16:12:08 CET 2020 Marcel Metz <mmetz@adrian-broher.net> - 1.61.0-1
- Initial package
- Replace github.com/gorilla/pat dependency with github.com/gorilla/mux
