{
  description = "pymenth - simple mental math trainer";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    pkgs = import nixpkgs { system = "x86_64-linux";};
    menth = pkgs.python3Packages.buildPythonPackage {
      pname = "pymenth";
      version = "0.1";
      src = ./.;
      pyproject = true;
      build-system = [pkgs.python3Packages.setuptools];
    };
  in {
    packages.x86_64-linux.default = menth;
  };
}
