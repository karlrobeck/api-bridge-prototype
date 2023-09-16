"use client";
import Link from 'next/link';
import React from 'react'
import { useState } from 'react';

const Layout = ({children}) => {

    const [mobileSidebar,setMobileSidebar] = useState(false);

  return (
    <main className='flex relative'>
        <aside className='sidebar hidden sm:block'>
            <section className='sidebar-content p-4'>
                <h1 className='font-bold text-xl'>Dashboard</h1>
                <div className='menu py-3'>
                    <ul className='menu-section'>
                        <Link href={'/dashboard/'} className='menu-item'>
                            Dashboard
                        </Link>
                        <Link href={'/dashboard/create'} className='menu-item'>
                            Create app
                        </Link>
                        <li className='menu-item'>
                            Applications
                        </li>
                        <li className='menu-item'>
                            Account
                        </li>
                    </ul>
                </div>
            </section>
        </aside>
        <div className='w-full'>
            {mobileSidebar && (
                <aside className='absolute sidebar block sm:hidden'>
                    <section className='sidebar-content p-4'>
                        <h1 className='font-bold text-xl space-x-3'>
                            <button onClick={() => setMobileSidebar(prev => !prev)} className='btn'>B</button>
                            <span>Dashboard</span>
                        </h1>
                        <div className='menu py-3'>
                            <ul className='menu-section'>
                                <Link href={'/dashboard/'} className='menu-item'>
                                    Dashboard
                                </Link>
                                <Link href={'/dashboard/create'} className='menu-item'>
                                    Create app
                                </Link>
                                <li className='menu-item'>
                                    Applications
                                </li>
                                <li className='menu-item'>
                                    Account
                                </li>
                            </ul>
                        </div>
                        <footer className='sidebar-footer mt-auto items-start gap-3'>
                            <div className='flex items-center gap-3'>
                            <img className='w-8 avatar-ring' src="https://static.vecteezy.com/system/resources/thumbnails/003/337/584/small/default-avatar-photo-placeholder-profile-icon-vector.jpg" alt="" />
                            Account name
                            </div>
                        </footer>
                    </section>
                </aside>
            )}
            <nav className='fixed navbar justify-between gap-3'>
                <button onClick={() => setMobileSidebar(prev => !prev)} className='btn block sm:hidden'>
                    Menu
                </button>
                <input placeholder='Search' className='input' type="text" />
            </nav>
            {children}
        </div>
    </main>
  )
}

export default Layout