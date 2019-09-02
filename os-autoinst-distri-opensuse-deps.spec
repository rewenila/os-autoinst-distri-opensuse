#
# spec file for package os-autoinst-distri-opensuse-deps
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           os-autoinst-distri-opensuse-deps
Version:        1
Release:        0
Summary:        Metapackage that contains the dependencies of os-autoinst-distri-opensuse
License:        MIT
Group:          Development/Tools/Other
BuildArch:      noarch
Url:            https://github.com/os-autoinst/os-autoinst-distri-opensuse
# BEGIN AUTOGENERATED DEPENDENCY LIST
Requires:       perl(Config::Tiny)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::file)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       perl(IO::File)
Requires:       perl(IO::Socket::INET)
Requires:       perl(List::Util)
Requires:       perl(LWP::Simple)
Requires:       perl(Perl::Critic::Freenode)
Requires:       perl(Selenium::Chrome)
Requires:       perl(Selenium::Remote::Driver)
Requires:       perl(Selenium::Remote::WDKeys)
Requires:       perl(Selenium::Waiter)
Requires:       perl(Test::Assert)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::Simple)
Requires:       perl(XML::Writer)
Requires:       perl(YAML::Tiny)
# END AUTOGENERATED DEPENDENCY LIST

%description
Metapackage that contains the dependencies of os-autoinst-distri-opensuse.

%prep

%build

%install

%check

%files

%changelog
