Feature: docker start script

Scenario: Starting the container incorrectly
    Given docker <images>
    And no environment is provided
    When I run the docker image
    Then the container prints: ERROR: To function correctly you must pass an environment variables of 'ServerIP' into the docker container
    And the container exits
    
    Examples:
    | images                |
    | diginc/pi-hole:alpine |
    | diginc/pi-hole:debian |


Scenario: Starting the container with defaults
    Given docker <images>
    And default environment is provided
    When I run the docker image
    Then the container started tini
    Then the container started tail
    Then the container started dnsmasq
    Then the container started <webserver>
    
    Examples:
    | images                | webserver |
    | diginc/pi-hole:alpine | nginx     |
    | diginc/pi-hole:debian | lighttpd  |


