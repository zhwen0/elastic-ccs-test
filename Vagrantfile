# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.synced_folder ".", "/vagrant", type: "rsync", 
    rsync__exclude: [".git/","es_installer","kb_installer","es_config"]
  config.vm.provision "shell", path: "provision_privileged.sh", privileged: true
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
  end

  config.vm.define "node1" do |node|
    node.vm.provider "virtualbox" do |v|
      v.name = "node1"
	  v.memory = "4096"
    end
	node.vm.provision "file", source: "es_installer", destination: "/home/vagrant"
	node.vm.provision "file", source: "es_config/elasticsearch1.yml", destination: "/home/vagrant/elasticsearch.yml"
    node.vm.provision "shell", path: "provision_elasticsearch.sh", privileged: false	
    node.vm.network "private_network", ip: "10.0.200.101"
    node.vm.hostname = "node1"
  end

  config.vm.define "node2" do |node|
    node.vm.provider "virtualbox" do |v|
      v.name = "node2"
	  v.memory = "4096"
    end
    node.vm.provision "file", source: "es_installer", destination: "/home/vagrant"
	node.vm.provision "file", source: "es_config/elasticsearch2.yml", destination: "/home/vagrant/elasticsearch.yml"
    node.vm.provision "shell", path: "provision_elasticsearch.sh", privileged: false
    node.vm.network "private_network", ip: "10.0.200.102"
    node.vm.hostname = "node2"
  end
  
  config.vm.define "nodekb" do |node|
    node.vm.provider "virtualbox" do |v|
      v.name = "Elastic Lab Kibana"
    end
	node.vm.provision "file", source: "kb_installer", destination: "/home/vagrant"
    node.vm.provision "shell", path: "provision_kibana.sh", privileged: false
    node.vm.network "private_network", ip: "10.0.200.110"
    node.vm.hostname = "nodekb"
  end
 
  config.vm.define "nodetest" do |node|
    node.vm.provider "virtualbox" do |v|
      v.name = "test"
	  v.memory = "4096"
    end
    node.vm.provision "file", source: "python", destination: "/home/vagrant"
    node.vm.network "private_network", ip: "10.0.200.111"
    node.vm.hostname = "nodetest"
  end
end
