#!/usr/bin/env bash
# make changes to config file using puppet

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"
	
	#SSH CLIENT CONFIGURATION
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
}
