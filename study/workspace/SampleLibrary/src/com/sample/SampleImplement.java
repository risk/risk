package com.sample;

import java.net.URL;
import java.net.URLClassLoader;

import com.sample.SampleCommon;
import com.sample.SampleInterface;;

public class SampleImplement implements SampleInterface {

	@Override
	public String message() {
		String m;

		URLClassLoader cl = (URLClassLoader)Thread.currentThread().getContextClassLoader();
		
		System.out.println("URLs ---A");
		URL[] path = cl.getURLs();
		for(URL p: path) {
			System.out.println(p.toString());		
		}
		System.out.println("--------");
		
		m = SampleCommon.createMessage(this);

		return m;
	}
}
