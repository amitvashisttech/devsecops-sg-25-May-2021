# -*- mode: ruby -*-
# vi: set ft=ruby :

ENV['VAGRANT_NO_PARALLEL'] = 'yes'

Vagrant.configure(2) do |config|

  config.vm.provision "shell", path: "bootstrap.sh"

  # Master Server
  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/xenial64"
    master.vm.hostname = "master.example.com"
    master.vm.network "private_network", ip: "172.31.0.100"
    master.vm.provider "virtualbox" do |v|
      v.name = "master"
      v.memory = 4048
      v.cpus = 2
      # Prevent VirtualBox from interfering with host audio stack
      v.customize ["modifyvm", :id, "--audio", "none"]
    end
    master.vm.provision "shell", path: "bootstrap_master.sh"
  end

  NodeCount = 2

  # Worker Nodes
  (1..NodeCount).each do |i|
    config.vm.define "worker#{i}" do |workernode|
      workernode.vm.box = "ubuntu/xenial64"
      workernode.vm.hostname = "worker#{i}.example.com"
      workernode.vm.network "private_network", ip: "172.31.0.10#{i}"
      workernode.vm.provider "virtualbox" do |v|
        v.name = "worker#{i}"
        v.memory = 1024
        v.cpus = 1
        # Prevent VirtualBox from interfering with host audio stack
        v.customize ["modifyvm", :id, "--audio", "none"]
      end
      workernode.vm.provision "shell", path: "bootstrap_worker.sh"
    end
  end

end
