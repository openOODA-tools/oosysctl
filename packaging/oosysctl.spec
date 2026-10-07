Name:           oosysctl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Inspects and sets Linux kernel parameters at runtime under /proc/sys/.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosysctl
Source0:        oosysctl-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosysctl is a sovereign, capability-bounded KERNEL PARAMS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosysctl
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosysctl-uninstall

%files
/usr/bin/oosysctl
/usr/bin/oosysctl-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
