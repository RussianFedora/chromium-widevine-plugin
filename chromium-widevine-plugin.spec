%global debug_package %{nil}

Summary:	Chromium WideVine plugin
Name:		chromium-widevine-plugin
Version:	1.4.9.1088
Release:	2%{?dist}

License:	Multiple, see https://chrome.google.com/
Url:		http://www.google.com/chrome
Group:		Applications/Internet
Source0:	https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

BuildRequires:	rpm cpio
ExclusiveArch:	x86_64

Requires:	chromium


%description
Official Widevine CDM plugin for Google's Open Source browser Chromium.

%prep
%setup -c -T


%build
rpm2cpio %{SOURCE0} | cpio -idmv


%install
mkdir -p %{buildroot}%{_libdir}/chromium/
install -m755 opt/google/chrome/libwidevinecdm.so %{buildroot}%{_libdir}/chromium/

%files
%dir %{_libdir}/chromium/
%{_libdir}/chromium/libwidevinecdm.so


%changelog
* Tue Jun  5 2018 Arkady L. Shane <ashejn@russianfedora.pro> 1.4.9.1088-2
- fix Chromium name

* Tue Jun  5 2018 Arkady L. Shane <ashejn@russianfedora.pro> 1.4.9.1088-1
- initial build
