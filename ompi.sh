# require autoconf libtool
./autogen.pl
./configure --prefix=$INSTALL_PREFIX --with-libevent=internal
make -j $(nproc) install
