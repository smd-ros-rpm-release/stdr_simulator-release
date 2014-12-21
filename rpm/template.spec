Name:           ros-indigo-stdr-server
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS stdr_server package

Group:          Development/Libraries
License:        GPLv3
URL:            http://stdr-simulator-ros-pkg.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-stdr-msgs
Requires:       ros-indigo-stdr-robot
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-map-server
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-stdr-msgs
BuildRequires:  ros-indigo-tf

%description
Implements synchronization and coordination functionalities of STDR Simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Chris Zalidis <zalidis@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

