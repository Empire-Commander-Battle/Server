(use-modules
 ((guix licenses) #:prefix license:)
 (guix packages)
 (guix gexp)
 (guix download)
 (guix git-download)
 (guix utils)
 (guix build-system gnu)
 (guix build-system meson)
 (guix build-system trivial)
 (gnu packages)
 (gnu packages admin)
 (gnu packages audio)
 (gnu packages autotools)
 (gnu packages base)
 (gnu packages bash)
 (gnu packages bison)
 (gnu packages cups)
 (gnu packages databases)
 (gnu packages fontutils)
 (gnu packages flex)
 (gnu packages image)
 (gnu packages gettext)
 (gnu packages ghostscript)
 (gnu packages gl)
 (gnu packages glib)
 (gnu packages gstreamer)
 (gnu packages gtk)
 (gnu packages kerberos)
 (gnu packages libusb)
 (gnu packages linux)
 (gnu packages mingw)
 (gnu packages openldap)
 (gnu packages perl)
 (gnu packages pulseaudio)
 (gnu packages pkg-config)
 (gnu packages python)
 (gnu packages mp3)
 (gnu packages photo)
 (gnu packages samba)
 (gnu packages scanner)
 (gnu packages sdl)
 (gnu packages tls)
 (gnu packages video)
 (gnu packages vulkan)
 (gnu packages xml)
 (gnu packages xorg)
 (ice-9 match)
 (srfi srfi-1))


(define-public wine-old
  (package
   (name "wine")
   (version "7.19")
   (source
    (origin
     (method url-fetch)
     (uri (let ((dir (string-append
		      (version-major version)
		      (if (string-suffix? ".0" (version-major+minor version))
			  ".0/"
			  ".x/"))))
	    (string-append "https://dl.winehq.org/wine/source/" dir
			   "wine-" version ".tar.xz")))
     (sha256
      (base32 "08cxigkd83as6gkqgiwdpvr7cyy5ajsnhan3jbadwzqxdrz4kb23"))))
   (build-system gnu-build-system)
   (native-inputs
    (list bison flex gettext-minimal perl pkg-config))
   (inputs
    ;; Some libraries like libjpeg are now compiled into native PE objects.
    ;; The ELF objects provided by Guix packages are of no use.  Whilst this
    ;; is technically bundling, it's quite defensible.  It might be possible
    ;; to build some of these from Guix PACKAGE-SOURCE but attempts were not
    ;; fruitful so far.  See <https://www.winehq.org/announce/7.0>.
    (list alsa-lib
	  cups
	  dbus
	  eudev
	  fontconfig
	  freetype
	  gnutls
	  gst-plugins-base
	  libgphoto2
	  openldap
	  samba
	  sane-backends
	  libpcap
	  libusb
	  libice
	  libx11
	  libxi
	  libxext
	  libxcursor
	  libxrender
	  libxrandr
	  libxinerama
	  libxxf86vm
	  libxcomposite
	  mit-krb5
	  openal
	  pulseaudio
	  sdl2
	  unixodbc
	  v4l-utils
	  vkd3d
	  vulkan-loader))
   (arguments
    (list
     ;; Force a 32-bit build targeting a similar architecture, i.e.:
     ;; armhf for armhf/aarch64, i686 for i686/x86_64.
     #:system (match (%current-system)
		((or "armhf-linux" "aarch64-linux") "armhf-linux")
		(x "i686-linux"))

     ;; XXX: There's a test suite, but it's unclear whether it's supposed to
     ;; pass.
     #:tests? #f

     #:configure-flags
     #~(list (string-append "LDFLAGS=-Wl,-rpath=" #$output "/lib/wine32"))

     #:make-flags
     #~(list "SHELL=bash"
	     (string-append "libdir=" #$output "/lib/wine32"))

     #:phases
     #~(modify-phases %standard-phases
		      ;; Explicitly set the 32-bit version of vulkan-loader when installing
		      ;; to i686-linux or x86_64-linux.
		      ;; TODO: Add more JSON files as they become available in Mesa.
		      #$@(match (%current-system)
			   ((or "i686-linux" "x86_64-linux")
			    `((add-after 'install 'wrap-executable
					 (lambda* (#:key inputs outputs #:allow-other-keys)
					   (let* ((out (assoc-ref outputs "out"))
						  (icd (string-append out "/share/vulkan/icd.d")))
					     (mkdir-p icd)
					     (copy-file (search-input-file
							 inputs
							 "/share/vulkan/icd.d/radeon_icd.i686.json")
							(string-append icd "/radeon_icd.i686.json"))
					     (copy-file (search-input-file
							 inputs
							 "/share/vulkan/icd.d/intel_icd.i686.json")
							(string-append icd "/intel_icd.i686.json"))
					     (wrap-program (string-append out "/bin/wine-preloader")
							   `("VK_ICD_FILENAMES" ":" =
							     (,(string-append icd
									      "/radeon_icd.i686.json" ":"
									      icd "/intel_icd.i686.json")))))))))
			   (x
			    `()))
		      (add-after 'unpack 'patch-SHELL
				 (lambda x
				   (substitute* "configure"
						;; configure first respects CONFIG_SHELL, clobbers SHELL later.
						(("/bin/sh")
						 (which "bash")))))
		      (add-after 'configure 'patch-dlopen-paths
				 ;; Hardcode dlopened sonames to absolute paths.
				 (lambda x
				   (let* ((library-path (search-path-as-string->list
							 (getenv "LIBRARY_PATH")))
					  (find-so (lambda (soname)
						     (search-path library-path soname))))
				     (substitute* "include/config.h"
						  (("(#define SONAME_.* )\"(.*)\"" x defso soname)
						   (format #f "~a\"~a\"" defso (find-so soname)))))))
		      (add-after 'patch-generated-file-shebangs 'patch-makedep
				 (lambda* (#:key outputs #:allow-other-keys)
				   (substitute* "tools/makedep.c"
						(("output_filenames\\( unix_libs \\);" all)
						 (string-append all
								"output ( \" -Wl,-rpath=%s \", so_dir );"))))))))
   (home-page "https://www.winehq.org/")
   (synopsis "Implementation of the Windows API (32-bit only)")
   (description
    "Wine (originally an acronym for \"Wine Is Not an Emulator\") is a
compatibility layer capable of running Windows applications.  Instead of
simulating internal Windows logic like a virtual machine or emulator, Wine
translates Windows API calls into POSIX calls on-the-fly, eliminating the
performance and memory penalties of other methods and allowing you to cleanly
integrate Windows applications into your desktop.")
   ;; Any platform should be able to build wine, but based on '#:system' these
   ;; are thr ones we currently support.
   (supported-systems '("i686-linux" "x86_64-linux" "armhf-linux"))
   (license license:lgpl2.1+)))

wine-old
