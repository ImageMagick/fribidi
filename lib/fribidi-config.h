/* @configure_input@ */
/* Not copyrighted, in public domain. */
#ifndef FRIBIDI_CONFIG_H
#define FRIBIDI_CONFIG_H

#define FRIBIDI "@PACKAGE@"
#define FRIBIDI_NAME "@PACKAGE_NAME@"
#define FRIBIDI_BUGREPORT "@PACKAGE_BUGREPORT@"

#define FRIBIDI_VERSION "@FRIBIDI_VERSION@"
#define FRIBIDI_MAJOR_VERSION @FRIBIDI_MAJOR_VERSION@
#define FRIBIDI_MINOR_VERSION @FRIBIDI_MINOR_VERSION@
#define FRIBIDI_MICRO_VERSION @FRIBIDI_MICRO_VERSION@
#define FRIBIDI_INTERFACE_VERSION @FRIBIDI_INTERFACE_VERSION@
#define FRIBIDI_INTERFACE_VERSION_STRING "@FRIBIDI_INTERFACE_VERSION@"

/* The size of a `int', as computed by sizeof. */
#define FRIBIDI_SIZEOF_INT @SIZEOF_INT@

/* Define if fribidi was built with MSVC */
@FRIBIDI_MSVC_BUILD_PLACEHOLDER@

#endif /* FRIBIDI_CONFIG_H */