Name:           ros-jade-keyboard
Version:        0.1.1
Release:        2%{?dist}
Summary:        ROS keyboard package

Group:          Development/Libraries
License:        GPLv2
URL:            http://wiki.ros.org/keyboard
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  rubygems

%description
publishes keyboard key presses

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Dec 05 2015 v01d <phreakuencies@gmail.com> - 0.1.1-2
- Autogenerated by Bloom

* Sat Dec 05 2015 v01d <phreakuencies@gmail.com> - 0.1.1-1
- Autogenerated by Bloom

* Sat Dec 05 2015 v01d <phreakuencies@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

