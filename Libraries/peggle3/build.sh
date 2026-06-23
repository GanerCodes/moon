#!/bin/bash -e
{ cd "${0%/*}"

# 󰤱  Cherrypick needed stuff from build/pyodide/dist and put them into 
#    a new dir "Out/Pyodide" and update paths (and fix jank within) Webinterface server
# 󰤱  Reduce size/load times of Pyodide/WASM ☾
# 󰤱􊽨 Redo peggle3.☾c to not use stack for rule result table as ☾ always needs large stack atm

NCORES=$(( $(nproc) - 1 )); [ "$NCORES" -lt 1 ] && NCORES=1

mkdir -p build Out
pushd build
  ☾ ../Libpeggle3/noparen.☾ "../Libpeggle3/peggle3" "./peggle3" || :
  gcc "./peggle3.c" -I"../Libpeggle3" -lpcre2-8 -Wno-implicit-int -shared -flto -fPIC -O3 -o "../Out/libpeggle3.so"
  
  mkdir -p pcre2-wasm
  pushd pcre2-wasm
    BUILD_PREFIX="$(pwd)/build"
    curl -L https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.46/pcre2-10.46.tar.bz2 -o pcre2.tar.bz2
    tar -xf pcre2.tar.bz2
    pushd pcre2-10.46
      export CFLAGS="-fPIC"
      export CXXFLAGS="-fPIC"
      emconfigure ./configure        --prefix="$BUILD_PREFIX" \
                  --enable-pcre2-8   --disable-pcre2-16       \
                  --disable-pcre2-32 --disable-shared --disable-jit
      emmake make -j$NCORES
      emmake make install
      popd
    popd
  emcc ./peggle3.c -I"../Libpeggle3"                       \
                   -I"./pcre2-wasm/build/include"          \
                     "./pcre2-wasm/build/lib/libpcre2-8.a" \
                   -sASSERTIONS=0 -sSTACK_OVERFLOW_CHECK=0 \
                   -sSIDE_MODULE=1 -sWASM_BIGINT           \
                   -Wno-implicit-int -fPIC -O3 -o ../Out/libpeggle3.wasm
  
  [ ! -d pyodide ] && git clone --recursive --depth=1 https://github.com/pyodide/pyodide
  pushd pyodide
    [ ! -d pyodide-recipes ] && git clone https://github.com/pyodide/pyodide-recipes
    sed -i -E 's/INITIAL_MEMORY=\w+/INITIAL_MEMORY=1GB/g;s/STACK_SIZE=\w+/STACK_SIZE=512MB/g' \
        Makefile.envs # 󷹇2𝕊, apparently -E doesn't take an argument so `-E ... -E ...` breaks stuff
    ./run_docker --non-interactive bash -c \
      "
        export EMSDK_NUM_CORE=$NCORES
        export EMCC_CORES=$NCORES
        export PYODIDE_JOBS=$NCORES
        pyodide build-recipes "regex,cffi,pycryptodome" --recipe-dir pyodide-recipes/packages --install
        make -j$NCORES
      "
    popd
  popd

exit $?; }