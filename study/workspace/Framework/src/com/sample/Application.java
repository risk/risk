package com.sample;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;

import com.sample.SampleInterface;

public class Application {

	URLClassLoader cl_;
	
	private void initilize() throws MalformedURLException {
		File jarCommonFile = new File(
				"/Users/risk/Develop/eclipse/workspace/lib/SampleCommon.jar");
		File jarImpleFile = new File(
				"/Users/risk/Develop/eclipse/workspace/lib/SampleImplement.jar");
		URL[] urls = {
				jarCommonFile.toURI().toURL(),
				jarImpleFile.toURI().toURL()};
		
		cl_ = new URLClassLoader(urls, ClassLoader.getSystemClassLoader());
	}
	
	private void run(String[] arg) {
		
		System.out.println("Library List -----");
		URL[] path = cl_.getURLs();
		for(URL url : path) {
			System.out.println(url.toString());		
		}
		System.out.println("test -----");
		
		try {
			Class<?> clazz = 
					cl_.loadClass("com.sample.SampleImplement");
			SampleInterface imp = (SampleInterface)clazz.newInstance();
			System.out.println(imp.message());
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (InstantiationException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Application app = new Application();
		try {
			app.initilize();
			app.run(args);
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
	}

}
