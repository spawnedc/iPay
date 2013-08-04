/* global module */
module.exports = function(grunt) {

	// Project configuration.
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		timestamp: grunt.template.today('yyyymmddhhMMssl'),

		devMediaDir: 'static-dev',
		devCssDir: 'static-dev/css',
		devScssDir: 'static-dev/scss',
		devJsDir: 'static-dev/js',
		devImgDir: 'static-dev/img',

		buildDir: 'static',
		builtCssDir: 'static/css',
		builtJsDir: 'static/js',
		builtImgDir: 'static/img',

		// We've got things in a /build/ dir so we can just chop that to return
		// to a clean state
		clean: ['<%= buildDir %>/'],

		jshint: {
			options: {
				boss: true,
				browser: true,
				curly: false,
				devel: true,
				eqeqeq: false,
				eqnull: true,
				expr: true,
				evil: true,
				immed: false,
				laxcomma: true,
				newcap: false,
				noarg: true,
				smarttabs: true,
				sub: true,
				undef: true
			},
			all: [
				'<%= devJsDir %>/**/*.js',
				'Gruntfile.js'
			]
		},

		sass: {
			dev: {
				files: {
					'<%= devCssDir %>/styles.css': '<%= devScssDir %>/styles.scss',
				},
				options: {
					style: 'expanded'
				}
			},
			build: {
				files: {
					'<%= builtCssDir %>/styles.css': '<%= devScssDir %>/styles.scss',
				},
				options: {
					style: 'compressed'
				}
			}
		},

		watch: {
			css: {
				files: [
					'<%= devScssDir %>/**/*.scss'
				],
				tasks: ['sass:dev']
			},
			scripts: {
				files: [
					'<%= devJsDir %>/**/*.js'
				],
				tasks: ['jshint']
			}
		},

		copy: {
			// Copy already minified javascript
			js: {
				files: [
					{
						dest: '<%= builtMediaDir %>/',
						src: ['js/*.*'],
						expand: true,
						cwd: '<%= devMediaDir %>/'
					}
				]
			}
		},

		shell: {
			// Shell command for running Django server
			devserver: {
				command: 'python manage.py runserver',
				options: {
					stdout: true,
					stderr: true
				}
			}
		},

		concurrent: {
			serve: {
				tasks: ['watch', 'shell:devserver'],
				options: {
					logConcurrentOutput: true
				}
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-copy');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-concurrent');
	grunt.loadNpmTasks('grunt-shell');

	// Here's our build process
	grunt.registerTask('build', [
		// Remove previously built files
		'clean',
		// Check all our JS is ship-shape – we skip some files in .jshintignore
		'jshint',
		// Copy things into the build dir (nothing special to do there)
		'copy',
		// Create our CSS files with sass
		'sass:build'
	]);

	// Default: build! Add `test` task to this when we have one
	// This will get called before deploying, so should do allthethings really
	grunt.registerTask('default', ['build']);

	// Local server task
	grunt.registerTask('serve', ['sass:dev', 'concurrent:serve']);
};
