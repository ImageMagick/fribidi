#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

URL = "https://github.com/fribidi/fribidi/releases/download/v{version}/fribidi-{version}.tar.xz"


def update_source(updater):
    updater.replace_source()
    updater.remove(".github")
    updater.update_config()


def create_config_header(updater):
    major, minor, micro = updater.version.split(".")
    updater.write_file("lib/fribidi-config.h", f"""/* @configure_input@ */
/* Not copyrighted, in public domain. */
#ifndef FRIBIDI_CONFIG_H
#define FRIBIDI_CONFIG_H

#define FRIBIDI "GNU FriBidi"
#define FRIBIDI_NAME "GNU FriBidi"
#define FRIBIDI_BUGREPORT "https://github.com/fribidi/fribidi/issues/new"

#define FRIBIDI_VERSION "{updater.version}"
#define FRIBIDI_MAJOR_VERSION {major}
#define FRIBIDI_MINOR_VERSION {minor}
#define FRIBIDI_MICRO_VERSION {micro}
#define FRIBIDI_INTERFACE_VERSION 5
#define FRIBIDI_INTERFACE_VERSION_STRING "4"

/* The size of a `int', as computed by sizeof. */
#define FRIBIDI_SIZEOF_INT 4

/* Define if fribidi was built with MSVC */
#define FRIBIDI_BUILT_WITH_MSVC

#endif /* FRIBIDI_CONFIG_H */
""")


updater = Updater(__file__, "fribidi", URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Updated fribidi to {version}"),
    Step("Create fribidi-config.h from fribidi-config.h.in and change the content",
        create_config_header, "Created fribidi-config.h from fribidi-config.h.in and changed the content."),
    updater.clone_dependencies_step(),
])
